# Hello Assignment

## Prerequisits

* Docker is installed

## To build a docker image

```shell script
docker build -t hello .
```

## To run the application in container

```shell script
docker run -dit -p 8080:8080 --name hello hello:latest
```

## Available endpoints

* /
* /healthz

## Answers

* What other information would you add to health endpoint json object in step 2? Explain what would be the use case for that extra information?

Depends on actual functionality. If app works with some cloud environment, make sense to check cloud availability. 
If it works with some database, check db access. If app calls another web servers, ping them. 

* How would you automate the build/test/deploy process for this application? (a verbal answer is enough. installation of CICD is bonus, not required)

Build and deploy - I would try Github Actions (never had a chance to do it)
Tests - Postman or Selenium or unit tests 

* What branching strategy would you use for development?

Master as main branch, develop as common developer branch, feature branches, fix branches, separate branches for releases

* What CICD tool/service would you use?

Any tools which is available: Jenkins, Bamboo, etc

* What stages would you have in the CICD pipeline?

Developer/QA/Production

* What would be the purpose of each stage in CICD pipeline

Developer - Integrate changes from all developers, QA - Testing, Production - ...