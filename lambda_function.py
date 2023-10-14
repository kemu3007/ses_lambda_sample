import boto3
from datetime import datetime


def lambda_handler(event, context):
    ses_client = boto3.client("ses", region_name="ap-northeast-1")
    today = datetime.today()
    subject = "タスク通知"
    messages = []
    if today.day == 18:
        messages.append("・Y's への請求書発行")
    elif today.day == 26:
        messages.append("・仕送り代金振込")
        messages.append("・駐車場代金振込")
        messages.append("・淡路島家賃振込")
        messages.append("・カーリース代金の引き落とし")
    if len(messages):
        response = ses_client.send_email(
            Destination={"ToAddresses": ["kemu430113@gmail.com"]},
            Message={
                "Body": {"Text": {"Charset": "UTF-8", "Data": "\n".join(messages)}},
                "Subject": {"Charset": "UTF-8", "Data": subject},
            },
            Source="tasks@trash-box.dev",
        )
    print(messages)
