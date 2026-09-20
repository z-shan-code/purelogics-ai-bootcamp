from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("crime-and-punishment.pdf")
pages = loader.load()
print(f"Number of Pages : {len(pages)}")
print("---- Sample from page 0 ----")
print(pages[0].page_content[:500])
print("---- Sample from a middle page ----")
print(pages[len(pages)//2].page_content[:500])