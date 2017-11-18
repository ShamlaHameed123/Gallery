# Gallery
INSTALL aws cli by the command sudo apt install awscli

# Sync S3 data with local folder
aws --no-sign-request s3 sync s3://schandra-test--files ./media/


# Migrate the data to DB for rating

Run the script copy_photos.py
