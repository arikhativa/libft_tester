
NAME=libft
IMG=arikhativa/libft-tester:0.0.1

MAKEFILE_PATH=$(abspath $(lastword $(MAKEFILE_LIST)))
CURRENT_DIR=$(notdir $(patsubst %/,%,$(dir $(MAKEFILE_PATH))))
FULL_PATH=$(shell pwd)

SRC=$(FULL_PATH)/src



.PHONY: build push run stop enter test valgrind review review/valgrind

build:
	docker build -t $(IMG) .

push:
	docker push $(IMG)

run:
	docker run -d -it -v $(HOME):$(WORKDIR)/ --name $(NAME) $(IMG)

stop:
	docker rm -f $(NAME)

re: stop run
	@true

enter:
	docker exec -it $(NAME) bash

test:
	python3 -B $(SRC)/main.py

valgrind:
	docker exec -it $(NAME) $(WORKDIR)/pool-tester/test.sh $(PROJ) $(WORKDIR)

review:
	./test.sh $(PROJ) ~/code_review

review/valgrind:
	docker exec -it $(NAME) $(WORKDIR)/pool-tester/test.sh $(PROJ) $(WORKDIR)/code_review
