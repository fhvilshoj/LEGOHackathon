import boto3

sqs = boto3.client('sqs')
queue_url = sqs.get_queue_url(QueueName='Team2_LEGOQueue.fifo')['QueueUrl']
print(queue_url)
while True:
    messages = sqs.receive_message(
            QueueUrl=queue_url, 
            MaxNumberOfMessages=1,
            MessageAttributeNames=['.*'])
    if 'Messages' in messages:
        for message in messages['Messages']:
            print("Message body: ", message['Body'])
            print("Message attribure ('product_id'): ", message['MessageAttributes']['product_id']['StringValue'])
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
    else:
        # Skip (No new messages in the queue)
        pass
