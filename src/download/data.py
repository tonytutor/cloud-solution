import os


CEN = "sas_centralus.txt"
EAS = "sas_eastasia.txt"
WES = "sas_westeurope.txt"


dlSas = {
    "w": WES,
    "c": CEN,
    "e": EAS
}

valid_sas = ["w", "c", "e"]


class Data:
    def __init__(self, dl_to="./data/", dl_sas="w"):
        if not os.path.exists(dl_to):
            os.system(f"mkdir -p {dl_to}")
        self.data_root = dl_to

        if dl_sas not in valid_sas:
            self.sas = dlSas["w"]
        else:
            self.sas = dlSas[dl_sas]

    def dl_data(self):
        print("Download data...")
        print(os.system(f"python src/download/download_data.py --sas-url 'https://cloudcoverdatawesteurope.blob.core.windows.net/public?se=2022-08-01T12%3A00Z&sp=rl&sv=2018-11-09&sr=c&sig=DrqaBLSI9t1nnx1sekyPaMgsqMiO9%2BBzjU/JwDhfQ64%3D'"))
        if len(os.listdir(self.data_root)) > 1:
            print("Done!")
