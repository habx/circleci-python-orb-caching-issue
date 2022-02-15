# circleci-python-orb-cache-bug

* CircleCI-Public/python-orb

Project for fix caching problem: https://github.com/CircleCI-Public/python-orb/pull/89#issuecomment-1034019711


```
error computing cache key: template: cacheKey:1:32: executing "cacheKey" at <checksum "/tmp/cci_pycache/lockfile">: error calling checksum: open /tmp/cci_pycache/lockfile: no such file or directory
```

 # Fixed !! 
 
- Fix with v2.0.1 : https://github.com/CircleCI-Public/python-orb/releases/tag/v2.0.1


