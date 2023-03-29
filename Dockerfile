# what exactly docker image: 
                # with the help of this file whatever information actually writing, it actuall creates a docker image and
                # that docker image can be taken and it can be run within a contianer 
                # it can be run as docker container in any operating system, supose if i also want to run in my local it we can run
                # run this entier docker image as a docker container which will be interacting with the kernel of our operating system 
                # kind of container which can independently run by comunncicating with the kernal of the operating system 

# The below commands are using to create the docker image
    # this command bassically to selct any kind of base image: from the docker hub take the image that has linux on top o it python 3.7 
FROM python:3.7
    # what ever code that we have in this repository and file in this repository have to copy to that image (form the current folder) put 
    # the app folder as the name we mentioned here
COPY . /app
    # the we create that as our working directory 
WORKDIR /app
    # we mentioning what are the dependencies we have to install, in this we will mention that requirement.txt will have all the dependencies 
    # we can set that as to run and install the all the packages to our project 
RUN pip install -r requirements.txt 
    # when the docker image run as the conainer, in oreder to access the application inside the container we have to expose some port 
    # then only we will be able to accesss the entier url, because that portal we will be able to access that apllication 
    #  so we here going to expose a port within that particular docker container and that port we mentioning here 
EXPOSE $PORT 
    # we finally mentioning that how the application going to run, how many workers going to hanlde the rewues, local host and the port number
    # and what is the application instance name inside the file we created (flask file that holding the application api implementations)
    # what is the binding is acually doing is very very important, because this is the localhost ip address that going to
    # assign in the cloud platform so we have to make sure our port to bind to that address in order to access the applicatiom
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app