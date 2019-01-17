from github import Github
import requests,json
import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--name', required=True, action='store', help='Username')
	parser.add_argument('-p', '--password', required=True, action='store', help='Password')
	parser.add_argument('-q', '--query', required=True, action='store', help='Word to be searched. Example: bot')
	parser.add_argument('-o', '--option', required=True, action='store', help='branch/star')
	my_args = parser.parse_args()
	return my_args


def brancher(topic, g):
	repos = g.search_repositories(topic)
	for r in repos:
		print("Branching:	" + r.name)
		g.get_user().create_fork(r)


def starrer(topic, g):
	repos = g.search_repositories(topic)
	for r in repos:
		print("Star-ing:	" + r.name)
		g.get_user().add_to_starred(r)


def main():
	args = get_args()
	g = Github(args.name,args.password)
	opt = args.option
	if (opt == "branch"):
		brancher(args.query, g)
	elif (opt == "star"):
		starrer(args.query, g)
	else:
		print("Possible options (-o): 'branch' or 'star'.")


if __name__ == "__main__":
	main()
