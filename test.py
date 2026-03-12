def search_ddgs(query, max_result_num=5):
    res = DDGS().text(
        query,
        region="ko-kr",
        safesearch="off",
        backend="duckduckgo"
    )
    return [