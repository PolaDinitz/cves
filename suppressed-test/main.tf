resource "aws_s3_bucket" "suppressed_test_a" {
  bucket = "suppressed-test-a"
  acl    = "public-read"
}

resource "aws_s3_bucket" "suppressed_test_b" {
  bucket = "suppressed-test-b"
  acl    = "public-read"
}
