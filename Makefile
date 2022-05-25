build:
	docker build -t nba-streamlit:latest .

run:
	docker run -p 8501:8501 nba-streamlit:latest