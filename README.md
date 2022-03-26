# xcpretty_fix

fix bugs for [xcpretty](https://github.com/xcpretty/xcpretty) without changing xcpretty.

- [x] fixed hidden `Undefined symbols` like [this issue](https://github.com/xcpretty/xcpretty/issues/380)

# usage

see `tests/test.sh` and copy.

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
