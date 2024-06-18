


def parse_authors_openalex(start_it: int=0) -> tp.Dict:
    """
    Парсинг авторов с openalex
    """
    save_dict_authors = {}
    for it, id in tqdm(enumerate(authors_id), total=len(authors_id)):
        if it < start_it:
            continue
        if id not in save_dict_authors:
            author = Authors()[id]
            try:
                save_dict_authors[id] = author
            except:
                print(f'exception: author {id} not found!')
                continue
                
        if it % 100 == 0 and it != start_it:
            pd.to_pickle(save_dict_authors, f'save_dict_authors_{it}.pkl')
    return save_dict_authors


def parse_papers_openalex() -> tp.Dict:
    """
    Парсинг статей с openalex
    """
    save_dict_papers = {}
    for it, id in tqdm(enumerate(articles_id.unique()), total=len(articles_id.unique())):
        if id not in save_dict_papers:
            paper = Works()[id]
            try:
                save_dict_papers[id] = paper
            except:
                print(f'exception: paper {id} not found!')
                continue
                
        if it % 3000 == 0 and it != 0:
            pd.to_pickle(save_dict_papers, f'save_dict_papers_{it}.pkl')
    pd.to_pickle(save_dict_papers, f'save_dict_papers.pkl')
    return save_dict_papers
