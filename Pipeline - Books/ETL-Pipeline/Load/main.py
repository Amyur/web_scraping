import pandas as pd 
from article import Article 
from base import Base, engine, Session


def main(file_name):
	Base.metadata.create_all(engine)
	session = Session()
	articles = pd.read_csv("{}.csv".format(file_name))

	for idx, row in articles.iterrows():
		print("Cargando idx {} en BD".format(row["idx"]))
		article = Article(row["idx"],
			              row["name"],
			              row["price"])

		session.add(article)

	session.commit()
	session.close()

if __name__=="__main__":
		page = int(input("Choose the site you want to load to a DataBase. buscalibre = 1, linio = 0: "))

		if page == 1:
			web_name = "buscalibre"
			file_name = "clean_buscalibre_data"
		else:
			web_name = "linio"
			file_name = "clean_linio_data"

		main(file_name)