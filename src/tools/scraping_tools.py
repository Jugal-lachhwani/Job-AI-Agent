from apify_client import ApifyClient
import os 

APIFY_TOKEN = os.getenv('APIFY_TOKEN') 
APIFY_ACTOR_NAME = os.getenv('APIFY_ACTOR_NAME')

def linkedin_scrapper(actor_input):
    apify_client = ApifyClient(APIFY_TOKEN)

    # Run an Actor with an input
    print("Running the Actor...")
    actor_name = APIFY_ACTOR_NAME
    actor_run = apify_client.actor(actor_name).start(run_input=actor_input)

    print("🚀 Actor was started")
    print("💾 Check your run here: https://console.apify.com/actors/runs/%(id)s" % {"id": actor_run["id"]})
    return apify_client.dataset(actor_run["defaultDatasetId"])