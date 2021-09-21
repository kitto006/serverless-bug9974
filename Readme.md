This code is to reproduce Serverless issue: https://github.com/serverless/serverless/issues/9974
The bug is, we cannot name the CloudWatch rule under -schedule (see serverless1.yml)
The work-around is use Serverless is 2.56.0

The current version (as of 2021-09-20) of Serverless is 2.59.0, the serverless1.yml syntax no longer works, must use the serverless2.yml syntax, but can no longer name the cloudwatch rule.  The result is the rule is serverless framework generated cloudwatch rule name "<service-name>-WarmUpPlugingDefaultEventsRuleSchedule1-xxxxxxxxx"


serverless1.yml  (works with serverless 2.56.0, doesn't work with 2.59.0)
    custom:
        warmup:
            default:
                enabled: true # Whether to warm up functions by default or not
                name: bug9974-warmer
                events:
                    - schedule: 
                        name: rule-warmer-bug-9974
                        description: bug9974-test
                        rate: rate(5 minutes)
                prewarm: true

serverless2.yml (works in all recent versions)
    custom:
        warmup:
            default:
                enabled: true # Whether to warm up functions by default or not
                name: bug9974-warmer
                events:
                    - schedule: 'rate(5 minutes)'
                prewarm: true


serverless3.yml 
    functions:
        warmup:
            default:
            enabled: true # Whether to warm up functions by default or not
            name: bug9974-warmer
            events:
                - schedule: 
                    name: rule-warmer-bug-9974
                    description: bug9974-test
                    rate: rate(5 minutes)
            prewarm: true



To reproduce the results

1) copy serverless<n>.yml to serverless.yml
2) edit <your-s3-bucket-for-serverless-deploy> to an s3 bucket with appropriate permission for serverless deploy
3) serverless deploy -v