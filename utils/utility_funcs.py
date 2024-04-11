import requests
import sys

from mention_members import MENTION_MEMBERS


def _prep_job_error_message():
    """
    JOBが失敗した場合の通知メッセージを作成する
    失敗した場合は運用メンバーへメンションする

    Returns:
        dict: 通知メッセージ
    """

    notification_msg = 'GCSへのデプロイ作業が失敗しました！Githubでご確認ください！'

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


def notify_message(webhook_url):
    """
    メッセージをteamsへ通知する

    Args:
        message (string): 通知するメッセージ
        webhook_url (string): teamsへの通知に利用するwebhookのURL
    """
    response = requests.post(
        webhook_url,
        json=_prep_job_error_message(),
    )
    print(f'response: {response}')


if __name__ == "__main__":

    # パラメータ解析
    webhook_url = sys.argv[1]

    # 関数実行
    notify_message(webhook_url)


