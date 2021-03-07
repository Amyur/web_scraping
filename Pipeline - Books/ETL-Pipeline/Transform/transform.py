import pandas as pd 

def main(file_name):
	df = read_data(file_name)
	transform = transf(df)
	save = save_csv(transform)


def read_data(file_name):
	return pd.read_csv("{}.csv".format(file_name))

def transf(df):
	df["price"] = (df["price"].apply(lambda name: name.split("$")[1])
               .map(lambda point:point.split("."))
               .map(lambda unit:''.join(unit)).astype(int))
	return df

def save_csv(transform):
	return transform.to_csv(r'C:\Users\Amylkar\Anaconda31\envs\platzi_data\books\clean_{}_data.csv'.format(web_name), encoding='utf-8', index = None, header=True)


if __name__=="__main__":
	page = int(input("Choose the site you want to transform. buscalibre = 1, linio = 0: "))

	if page == 1:
		web_name = "buscalibre"
		file_name = "buscalibre_data"
	else:
		web_name = "linio"
		file_name = "linio_data"

	main(file_name)
