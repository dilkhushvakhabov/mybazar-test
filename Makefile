.PHONY: run test

# Run the main application
run:
	docker-compose up

# Run tests
test:
	docker-compose -f docker-compose.test.yml up
