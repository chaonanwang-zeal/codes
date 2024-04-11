import requests

# from notification_settings import (
#     MAIN_NOTIFICATION_TEAM_URL,
#     MENTION_MEMBERS,
# )
# JOB成功・失敗を通知するWebhook URL
MAIN_NOTIFICATION_WEBHOOK_URL = (
    'https://avantg.webhook.office.com/webhookb2'
    '/87c2db7e-f692-446f-86fd-2d5817ac89af@c120f892-e83d-4d2d-b663-cd7a76efc4ea'
    '/IncomingWebhook/9541568aa1624155a8b451aa3fecf6a0/5607e0eb-cc9a-43f7-ae9a-7f64075cb93e'
)

# JOB失敗の際にメンションするメンバー一覧
MENTION_MEMBERS = [
    'chaonan.wang@avantcorp.com',
]


def _prep_job_error_message(job_name):
    """
    JOBが失敗した場合の通知メッセージを作成する
    失敗した場合は運用メンバーへメンションする

    Args:
        job_name (str): 通知するJOB名

    Returns:
        dict: 通知メッセージ
    """

    notification_msg = f'【{job_name}】 が失敗しました！！！'

    entries = []
    for m in MENTION_MEMBERS:
        entries.append(
            {
                'type': 'mention',
                'text': f'<at>{m}</at>',
                'mentioned': {
                    'id': m,
                    'name': m.split('@')[0]
                },
            }
        )
    mentions = ''.join([f'<at>{m}</at> ' for m in MENTION_MEMBERS])

    message = {
        'type': 'message',
        'attachments': [{
            'contentType': 'application/vnd.microsoft.card.adaptive',
            'content': {
                'type': 'AdaptiveCard',
                'body': [{
                    'type': 'TextBlock',
                    'text': f'{mentions}\n\n{notification_msg}\n\n',
                }],
                '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
                'version': '1.0',
                'msteams': {
                    'entities': entries,
                    'width': 'Full',
                },
            },
        }],
    }

    return message

def notify_message(message, webhook_url):
    """
    メッセージをteamsへ通知する

    Args:
        message (string): 通知するメッセージ
        webhook_url (string): teamsへの通知に利用するwebhookのURL
    """
    response = requests.post(
        webhook_url,
        json=message,
    )
    print(f'response: {response}')

def notify_job_error(job_name, webhook_url=MAIN_NOTIFICATION_WEBHOOK_URL):
    """
    JOBが失敗した場合の通知メッセージを作成する
    失敗した場合は運用メンバーへメンションする

    Args:
        job_name (str): 通知するJOB名
        webhook_url (string): teamsへの通知に利用するwebhookのURL
    """

    notify_message(_prep_job_error_message(job_name), webhook_url)


notify_job_error('GCSへのデプロイ作業')

