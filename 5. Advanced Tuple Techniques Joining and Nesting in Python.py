# Task 1: Product Catalog Merging

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
catalog3 = (("PC", 700), ("Headset", 300))

def merge_catalogs(*args):
    catalog_list = list(args)
    merged_catalog = []
    for catalog in catalog_list:
        merged_catalog += catalog

    print(tuple(merged_catalog))

merge_catalogs(catalog1, catalog2, catalog3)