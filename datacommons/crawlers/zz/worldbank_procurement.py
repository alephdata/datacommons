import json
from normality import slugify


def parse(context, data):
    table = context.datastore["zz_worldbank_procurement"]
    with context.load_file(data["content_hash"], read_mode="rt") as json_file:
        json_data = json.load(json_file)
        columns_data = json_data["meta"]["view"]["columns"]
        columns = [slugify(col["name"], sep="_") for col in columns_data]
        for item in json_data["data"]:
            award = dict(zip(columns, item))
            table.upsert(award, ["id"])
