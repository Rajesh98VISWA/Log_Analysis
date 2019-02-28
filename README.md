# Log_Analysis
### By N N V Viswanadha Rajesh

Log Analysis Project, Is a small part of project that belongs to Udacity [Full Stack Web Developer : Nanodegree]

## Analysis for Report :

<h1 align="center">
  <a href="https://github.com/Rajesh98VISWA/Log_Analysis"><img src="http://mathalope.co.uk/wp-content/uploads/2015/04/python-udacity-672x299.png" alt="python-icon" width="500"></a>
  <br>

A Reporting page that prints out reports in a plain text format based on the data in the database. This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Answers Provided to following questions:

1. What are the most popular three aricles of all time?
   
2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?
   

## Tools Used :

* Python3
* VirtualBox
* Vagrant
* Git
* PostgreSQL
* Text Editor(Sublime text)

## Content :

In this project consists for following files:

* news.py - It is a main file to run Logs Analysis Reporting Tool

* output.txt - It is a output file that will shown on the git bash

* README.md - It is an Instructions to install this reporting tool

## Installing Phase

There are some urls and a few instructions on how to run the project

## Links Used -[URL's] :
- [Git](https://git-scm.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/)
- [Vagrantfile](https://https://github.com/udacity/fullstack-nanodegree-vm)
- [Sublime Text](https://www.sublimetext.com/3)

## Installing Process

* Install Git, Sublime text, VirtualBox and Vagrant
* Clone the Udacity Vagrantfile
* Goto Vagrant dictory and download the zip file and place here 
* Open terminal or git
* Launch the Vagrant VM(`vagrant up`)
* Run Vagrant VM(`vagrant ssh`)
* Now change the directory into vagrant folder i.e., `cd /vagrant`

#### brief on project
> This project is written in python 
> using database (can be anything either software based or written format )
> major requirement is psycopg2 module
> This project is developed in windows 10 os
> using sublime text application
> compiled in gitbash


## Project Deployement

Download the project zip file and unzip the file now copy unzip file inside `vagrant/Log-Analysis`

1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command.

```
$ vagrant up
```
2. Now log into vagrant using below command

```
$ vagrant ssh
```
3. Download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

4. Unzip downloaded file. The file inside is called newsdata.sql

5. Copy the newsdata.sql file and place inside `vagrant/Log-Analysis` 

6. cd into the correct project directory `vagrant/Log-Analysis`

7. Load the data in local database using the command:

```
$ psql -d news -f newsdata.sql
```
8. Run newsdata.py using:

```
$ python news.py
```
Note: queries will take sometime to execute

### Run [Execution] :
  1. From the vagrant directory inside the virtual machine,run news.py using:
  ```
    $ python3 news.py
  ```

## Varied Proficiency

This README document is based on a template suggested by PhilipCoach in this Udacity from [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524).



