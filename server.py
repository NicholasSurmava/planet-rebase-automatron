from src import create_app

app = create_app()

if __name__ == '__main__':
    app.logger.info('Dev server started...')
    app.run(debug=True)
