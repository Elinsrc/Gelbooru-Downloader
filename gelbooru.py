import requests, json, random, os, asyncio
from pySmartDL import SmartDL

tags = input("Gelbooru Downloader\nCreated By Elinsrc\nПример: neko\nЗапрос(теги): ")
pid = input("Номер страницы(по умолчанию: 0): ")

directory = "Gelbooru_downloads/"

async def main():
    data = requests.get("https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags={}&pid={}".format(tags, pid)).json()

    img_data = data["post"]
    image = random.choice(img_data)

    if not os.path.exists(os.path.dirname(directory)):
        os.makedirs(os.path.dirname(directory))

    for i in data["post"]:
        file_dir = directory + i["image"]
        url = "https://img3.gelbooru.com/images/{}/{}".format(i["directory"], i["image"])

        if os.path.exists(file_dir):
            print("Сушествуюший файл: {}".format(file_dir))
            continue

        downloader = SmartDL(url, directory + i["image"], progress_bar=True, timeout=10, verify=False)
        print("\nЗагрузка файла: " + i["image"])
        downloader.start()

    print("\nФайлы сохраненны в папку " + directory)

if __name__ == "__main__":
    asyncio.run(main())
