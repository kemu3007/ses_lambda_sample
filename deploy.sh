source .env
pip install --platform manylinux2014_x86_64 --only-binary :all: -t package -r requirements.txt

cd package
zip -r ../function .

cd ..
zip function.zip lambda_function.py

aws lambda update-function-code --function-name ${LAMBDA_FUNCTION_NAME} --zip-file fileb://function.zip