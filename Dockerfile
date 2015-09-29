FROM tomcat:8-jre8
MAINTAINER Stephan Zednik "zednis2@rpi.edu"
ENV REFRESHED_AT 2015-09-28

ENV ELDA_VERSION 1.3.17

COPY elda/elda-standalone/target/elda-standalone /usr/local/tomcat/webapps/elda
#COPY spec/lva.spec.ttl /usr/local/tomcat/webapps/elda/specs/dcmp.ttl

EXPOSE 8080
CMD ["catalina.sh", "run"]