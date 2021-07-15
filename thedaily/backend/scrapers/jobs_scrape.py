from typing import List

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from random_user_agent.params import OperatingSystem
from random_user_agent.user_agent import UserAgent

from ..models import JobPost

BASE_URL = "https://www.indeed.com"


def get_top_jobs_from_indeed() -> List[str]:
    """
    This function scrapes google news for top news in any topic.

    Returns
    -------
    news: List
        A list of jobs around the location from the ip
    """
    url = BASE_URL + "/jobs?l=remote&sort=date"
    agent = UserAgent(operating_systems=[OperatingSystem.LINUX.value]).get_random_user_agent()

    response = requests.get(url, headers={'User-Agent': agent}, allow_redirects=True)
    soup = BeautifulSoup(response.text, 'html.parser')

    return list(map(sterilize_job, soup.find_all("div", {"class": "job_seen_beacon"})))


def sterilize_job(job: Tag) -> JobPost:
    """This function coverts bs4 tag to a sterilized model object"""
    url = BASE_URL + job.find("a", {"class": ""}).get("href")
    title = job.find("h2").find_all("span")[-1].text
    company = job.find("a").text.split(",")[0]

    return JobPost(job_url=url, job_title=title, company_name=company)
