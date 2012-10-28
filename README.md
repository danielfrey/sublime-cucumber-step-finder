# Sublime Text 2 plugin: Cucumber Step Finder

This plugin supports Rails developers to easily navigate to their cucumber (http://cukes.info) steps.

It provides a command, listing all steps in the open project and lets you choose
a step using the built-in mechanism for search.

#Installation
## Mac OSX (manual)
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    git clone git://github.com/danielfrey/sublime-cucumber-step-finder.git CucumberStepFinder

## Linux/Windows
Not tested yet. Contributions are welcome. If keyboard settings are provided, it should work.



## Package manager
As soon as it's listed in the Package Manager Channel I will update this section...

## Usage
The default key-binding is `cmd+y`
Change it if it's already used in your configuration

## Configuration
Two settings are available so far.

    {
       "cucumber_features_path"  :  "features",
       "cucumber_step_pattern"   :  ".*_steps.*\\.rb"
    }

The plugin looks for `cucumber_features_path` as a direct subdirectory of your project as it's the default in Rails projects. Override this setting of your steps are located in a different subdirectory.

In the given features directory it uses the secod setting for finding step-files recursively matching the `cucumber_step_pattern`

