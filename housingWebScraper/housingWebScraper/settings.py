

BOT_NAME = 'housingWebScraper'

SPIDER_MODULES = ['housingWebScraper.spiders']
NEWSPIDER_MODULE = 'housingWebScraper.spiders'


ROBOTSTXT_OBEY = True

# CSV settings
CSV_DELIMITER = "|"

# CSV output folder
CSV_OUTPUT_FOLDER = "housingWebScraper/output/"

# FEED EXPORTING
FEED_EXPORTERS = {
    'custom_csv': 'housingWebScraper.exporters.CsvOptionRespectingItemExporter'
}


ITEM_PIPELINES = {
    'housingWebScraper.pipelines.HousingwebscraperPipeline': 300,
    'housingWebScraper.pipelines.MultiCSVItemPipeline': 300
}
