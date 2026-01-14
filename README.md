# RAG using InterSystems IRIS Vector Search
This is the repository containing the application code that appears in the [RAG using InterSystems IRIS Vector Search](https://play.instruqt.com/embed/intersystems/tracks/iris-vector-search?token=em_qN1o8JoexIbVXonM) tutorial. If you're interested in completing the tutorial, or would like to see the other InterSystmes IRIS tutorials available, check out our [Developer Hub](https://developer.intersystems.com).

This repo includes code required for each challenge individually, in the state it's in at the beginning of each challenge, so the files may not be fully functional as-is and should be considered for demonstration purposes only. The `final` folder contains a "finished" `app.py` file that represents all of the work done as a part of the tutorial; after installing the dependencies, this file can be run as a fully functional app if you're looking to test out the application locally.
## Getting Started
The demo RAG chat app is a streamlit app written in Python that leverages InterSystems IRIS as a vector database. You must have the Community Edition of InterSystems IRIS installed to use this app; check out [this article]((https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=ACLOUD#ACLOUD_image) for more information on installing and configuring InterSystems IRIS.
### Quickstart
1. Clone the repo
```sh
git clone https://github.com/dk-gervais/Vector-Search.git
```
2. Install dependencies
```sh
pip install -r requirements.txt
```
3. Create a `.env` file containing your InterSystems IRIS connection details (NOTE: The listed username/password are the default for new IRIS installations; your actualy username/password may differ from this command)
```sh
cat > .env << EOF
OPENAI_API_KEY={your OpenAI API key}
IRIS_USER=_SYSTEM
IRIS_PASSWORD=SYS
EOF
```
4. Run the app using streamlit
```sh
streamlit run src/final/final_app.py --server.port 8080
```
