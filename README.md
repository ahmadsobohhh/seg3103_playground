 Run Junit:
 
 
# Remove any class files from dist

rm -f ./dist/*.class

# Compile the application

javac -encoding UTF-8 --source-path src -d dist src/*.java

# Compile the tests

javac -encoding UTF-8 --source-path test -d dist -cp dist:lib/junit-platform-console-standalone-1.7.1.jar test/*.java

java -jar lib/junit-platform-console-standalone-1.7.1.jar --class-path dist --scan-class-path
