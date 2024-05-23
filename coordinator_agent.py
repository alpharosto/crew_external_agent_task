from email_content_agent import EmailContentAgent
from email_sender_agent import EmailSenderAgent

class CoordinatorAgent:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.email_content_agent = EmailContentAgent(verbose=verbose)
        self.email_sender_agent = EmailSenderAgent(verbose=verbose)

    def run(self, weather_data, recipient):
        if self.verbose:
            print("CoordinatorAgent: Starting workflow...")
        email_content = self.email_content_agent.generate_email_content(weather_data)
        self.email_sender_agent.send_email(email_content, recipient)
        if self.verbose:
            print("CoordinatorAgent: Workflow completed.")
