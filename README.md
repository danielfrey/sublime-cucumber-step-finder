# Sublime Text 2/3 plugin: Cucumber Step Finder

This plugin supports Rails developers to easily navigate to their cucumber (http://cukes.info) steps.

It provides by now two commands

* One listing all steps in the open project and letting you choose
a step using the built-in mechanism for search.
* The second one letting you jump to the corresponding step by calling the "MatchStep"-Command when standing
on a step in the features file

#Installation
## Mac OSX (manual)
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    git clone git://github.com/danielfrey/sublime-cucumber-step-finder.git CucumberStepFinder

## Linux/Windows
Not tested yet. Contributions are welcome. If keyboard settings are provided, it should work.

## Package Control
Installation through [package control](http://wbond.net/sublime_packages/package_control) is recommended. It will handle updating your packages as they become available. To install, do the following.

* In the Command Palette, enter `Package Control: Install Package`
* Search for `CucumberStepFinder`

## Usage
The default key-binding for "search" is `super + y` (`ctrl + alt + y`), respectively
`ctrl + super + m` (`ctrl + shift + m`) for "match".
Change it if one is already used in your configuration

Alternatively super+click the line in a features file to find it's definition (OSX)

## Configuration
The following settings are available so far.

    {
       "cucumber_features_path"  :  "features",
       "cucumber_step_pattern"   :  ".*_steps.*\\.rb",
       "cucumber_code_keywords"  :  ["given", "when", "then", "and","but", "und", "dann", "wenn", "gegeben sei", "angenommen"]
    }

The plugin looks for `cucumber_features_path` as a direct subdirectory of your project as it's the default in Rails projects. Override this setting if your steps are located in a different subdirectory.

In the given features directory it uses the second setting for finding step-files recursively matching the `cucumber_step_pattern`

For finding the matching step, CucumberStepFinder needs to know which are the cucumber-keywords. Since there are different keywords beside English, you can configure them in `cucumber_code_keywords`.
By default English and German are predefined.

To find out, which keywords to configure e.g. German (language code `de),
type

    cucumber --i18n de

 into the console. The last argument is the language code.
 Add all words marked with "code" to the settings.

### Project Specific Configuration
These settings can be changed globally, or in your `.sublime-project` file.

    "settings":
    {
      "CucumberStepFinder":
      {
        "cucumber_step_pattern": ".*\\.rb"
      }
    }
