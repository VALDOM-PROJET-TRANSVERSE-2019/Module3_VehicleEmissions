import pandas as pd
import re
import urllib
import os

car_type = ["berline", "break", "minispace", "monospace compact", "combispace", "tous-terrains", "monospace",
            "cabriolet", "coupe", "minibus"]
images_directory = "../vehicle_images/"


for car in car_type:
    f = open("scraped_url/" + car + ".txt", "rt")
    f_out = open("scraped_url/car.csv", "wt")

    for line in f:
        f_out.write(re.sub(f'[\t ]+', ",", line))
    f.close()
    f_out.close()

    car_df = pd.read_csv("scraped_url/car.csv")
    os.mkdir(images_directory + car)
    it = 1
    try:
        for site in car_df["site"]:
            urllib.request.urlretrieve(site, images_directory + car + "/"f"{it:04}" + ".jpg")
            it += 1
    except:
        print("404")
