class EmailContentAgent:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def generate_email_content(self, weather_data):
        if self.verbose:
            print("Generating email content...")
        content = f"Weather Alert for {weather_data['location']}:\n" \
                  f"Forecast: {weather_data['forecast']}\n" \
                  f"Temperature: {weather_data['temperature']}"
        if self.verbose:
            print(f"Generated email content: {content}")
        return content
