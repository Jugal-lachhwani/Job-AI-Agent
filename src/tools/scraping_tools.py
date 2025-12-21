"""
Web Scraping Tools Module.

This module provides tools for scraping job listings from LinkedIn
using the Apify platform.
"""

import logging
import os
from apify_client import ApifyClient

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
APIFY_TOKEN = os.getenv('APIFY_TOKEN') 
APIFY_ACTOR_NAME = os.getenv('APIFY_ACTOR_NAME')


def linkedin_scrapper(actor_input: dict):
    """
    Scrape LinkedIn job listings using Apify Actor.
    
    This function uses the Apify platform to run a LinkedIn scraping actor
    that searches for jobs based on the provided input parameters.
    
    Args:
        actor_input (dict): Dictionary containing job search parameters.
            Expected keys include:
            - title: Job title to search for
            - location: Geographic location
            - datePosted: Date range filter
            - experienceLevel: Experience level filters
            - remote: Remote work type filters
            - limit: Maximum number of results
            
    Returns:
        ApifyDataset: Dataset object containing scraped job listings.
        Use dataset.iterate_items() to access individual job records.
        
    Raises:
        ValueError: If APIFY_TOKEN or APIFY_ACTOR_NAME not configured.
        ApifyClientError: If scraping fails or actor errors occur.
        
    Example:
        >>> job_params = {
        ...     'title': 'Data Scientist',
        ...     'location': 'India',
        ...     'limit': 10
        ... }
        >>> dataset = linkedin_scrapper(job_params)
        >>> for job in dataset.iterate_items():
        ...     print(job['title'])
    """
    # Validate environment variables
    if not APIFY_TOKEN:
        logger.error("APIFY_TOKEN environment variable not set")
        raise ValueError("APIFY_TOKEN environment variable is required")
    
    if not APIFY_ACTOR_NAME:
        logger.error("APIFY_ACTOR_NAME environment variable not set")
        raise ValueError("APIFY_ACTOR_NAME environment variable is required")
    
    logger.info("Initializing Apify client for LinkedIn scraping")
    logger.debug(f"Actor input parameters: {actor_input}")
    
    try:
        # Initialize Apify client
        apify_client = ApifyClient(APIFY_TOKEN)

        # Run the Actor with input parameters
        logger.info(f"Starting Apify Actor: {APIFY_ACTOR_NAME}")
        actor_name = APIFY_ACTOR_NAME
        actor_run = apify_client.actor(actor_name).start(run_input=actor_input)

        logger.info(f"🚀 Actor started successfully. Run ID: {actor_run['id']}")
        logger.info(f"💾 Monitor run at: https://console.apify.com/actors/runs/{actor_run['id']}")
        
        # Return dataset for iteration
        dataset = apify_client.dataset(actor_run["defaultDatasetId"])
        logger.info(f"Dataset ID: {actor_run['defaultDatasetId']}")
        
        return dataset
        
    except Exception as e:
        logger.error(f"Failed to scrape LinkedIn jobs: {str(e)}", exc_info=True)
        raise