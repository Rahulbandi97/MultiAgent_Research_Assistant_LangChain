from src.tools.tools import web_search, scrape_url
from src.pipelines.pipeline import research_report_pipeline

# websearch_output = web_search("What is the latest research on AI?")
# print(websearch_output)

# scrape_output = scrape_url("https://www.nature.com/subjects/machine-learning")
# print(scrape_output)

# web_search_invoke = web_search.invoke("What is the latest research on AI?")
# print(web_search_invoke) 

topic = "The impact of AI on healthcare and medical research in 2026"
research_report_pipeline(topic)