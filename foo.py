

invocation_count = 0

def lambda_handler(event, context):
    global invocation_count

    invocation_count += 1

    return f"invocation_count = {invocation_count}"

