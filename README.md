# shiosaba
Shiosaba is a Rest API to make a phone call based on mackerel's webhook alert.

**Requires Serverless >= v1.12**

## Install
```
$npm install serverless -g
```

```
$npm install serverless-python-requirements
```

## Deploy to cloud provider
```
$sls deploy -v
```

## Function deployed!
```
https://xyz.amazonaws.com/prd/mackerel
```

## Notification setting
Set up the config.yml file of the notification destination in s3 bucket.

Add the address to your `config.yml`:

```config.yml
---
service: hoge
voice: null
notifications:
- name: bob
  tel: 819031111111
- name: alice
  tel: 811111117895
---
```

NOTE:Buckets are specified in BUCKET_NAME of `serverless.yml`
