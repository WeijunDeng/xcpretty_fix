fix bugs for xcpretty

- [x] fixed hidden `Undefined symbols`

# Usage

see `tests/test.sh`

```
bash tests/test.sh
```

```
+ cat tests/xcodebuild.log
+ xcpretty

❌  ld: symbol(s) not found for architecture armv7



❌  clang: error: linker command failed with exit code 1 (use -v to see invocation)


+ cat tests/xcodebuild.log
+ scripts/xcpretty_fix.sh

❌  ld: Undefined symbols for architecture armv7:



❌  ld:   "_kQYPublisherVoteComonentDeleted", referenced from:



❌  ld:       -[QYPHAssetsPickerViewController initWithSettings:] in libQYPhoto.a(QYPHAssetsPickerViewController.o)



❌  ld: symbol(s) not found for architecture armv7



❌  clang: error: linker command failed with exit code 1 (use -v to see invocation)
```
