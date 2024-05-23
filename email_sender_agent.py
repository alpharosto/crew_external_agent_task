class EmailSenderAgent:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def send_email(self, email_content, recipient):
        if self.verbose:
            print("Sending email...")
        print(f"Email sent to {recipient} with content:\n{email_content}")
