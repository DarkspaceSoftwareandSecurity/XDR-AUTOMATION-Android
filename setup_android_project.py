import os

# Define the base directory for the Android project
base_dir = r"C:\AndroidProjects\MyUpdatedAndroidApp"

# Directory structure for a modern Android project
directories = [
    "app/src/main/java/com/example/myapp",
    "app/src/main/res/layout",
    "app/src/main/res/values",
    "app/src/main/res/drawable",
    "app/src/main/assets",
    "gradle/wrapper"
]

# Create all directories with detailed logging
print("Starting to create directories...")
for dir_path in directories:
    full_path = os.path.join(base_dir, dir_path)
    if not os.path.exists(full_path):
        try:
            os.makedirs(full_path, exist_ok=True)
            print(f"Created directory: {full_path}")
        except Exception as e:
            print(f"Failed to create directory {full_path}: {e}")
    else:
        print(f"Directory already exists: {full_path}")

# Function to create a file if it does not exist
def create_file_if_not_exists(file_path, content):
    if not os.path.exists(file_path):
        try:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Created file: {file_path}")
        except Exception as e:
            print(f"Failed to create file {file_path}: {e}")
    else:
        print(f"File already exists: {file_path}")

# Create AndroidManifest.xml
print("\nCreating AndroidManifest.xml...")
android_manifest_content = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapp">

    <application
        android:allowBackup="true"
        android:label="XDR Security App"
        android:supportsRtl="true"
        android:theme="@style/Theme.MyApp">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
"""
manifest_path = os.path.join(base_dir, "app/src/main/AndroidManifest.xml")
create_file_if_not_exists(manifest_path, android_manifest_content)

# Create build.gradle for app module with updated settings for Compose and Kotlin
print("\nCreating app/build.gradle for app module...")
app_gradle_content = """plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.myapp"
    compileSdk = 33

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 21
        targetSdk = 33
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        vectorDrawables {
            useSupportLibrary = true
        }
    }

    buildTypes {
        release {
            // Updated: Correct usage of minifyEnabled without prefix 'is'
            minifyEnabled false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
        debug {
            minifyEnabled false
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }

    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.4.3"
    }

    packagingOptions {
        resources {
            excludes.add("/META-INF/{AL2.0,LGPL2.1}")
        }
    }
}

dependencies {
    implementation "androidx.core:core-ktx:1.10.1"
    implementation "androidx.appcompat:appcompat:1.6.1"
    implementation "com.google.android.material:material:1.9.0"
    implementation "androidx.constraintlayout:constraintlayout:2.1.4"
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.6.1"
    implementation "androidx.compose.ui:ui:1.4.3"
    implementation "androidx.compose.material3:material3:1.1.0-alpha04"
    implementation "androidx.activity:activity-compose:1.7.1"
    testImplementation "junit:junit:4.13.2"
    androidTestImplementation "androidx.test.ext:junit:1.1.5"
    androidTestImplementation "androidx.test.espresso:espresso-core:3.5.1"
    androidTestImplementation "androidx.compose.ui:ui-test-junit4:1.4.3"
}
"""
app_gradle_path = os.path.join(base_dir, "app/build.gradle")
create_file_if_not_exists(app_gradle_path, app_gradle_content)

# Create root-level build.gradle file with plugin repositories
print("\nCreating root build.gradle...")
root_gradle_content = """buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath "com.android.tools.build:gradle:8.1.1"
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.21"
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
"""
root_gradle_path = os.path.join(base_dir, "build.gradle")
create_file_if_not_exists(root_gradle_path, root_gradle_content)

# Create settings.gradle
print("\nCreating settings.gradle...")
settings_gradle_content = """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "MyUpdatedAndroidApp"
include(":app")
"""
settings_gradle_path = os.path.join(base_dir, "settings.gradle")
create_file_if_not_exists(settings_gradle_path, settings_gradle_content)

# Create gradle-wrapper.properties for wrapper configuration
print("\nCreating gradle-wrapper.properties...")
gradle_wrapper_properties_content = """distributionUrl=https\://services.gradle.org/distributions/gradle-8.1-bin.zip
"""
gradle_wrapper_properties_path = os.path.join(base_dir, "gradle/wrapper/gradle-wrapper.properties")
create_file_if_not_exists(gradle_wrapper_properties_path, gradle_wrapper_properties_content)

# Create MainActivity.java for XDR data collection, analysis, and response
print("\nCreating MainActivity.java...")
main_activity_content = """package com.example.myapp;

import android.os.Bundle;
import androidx.activity.ComponentActivity;
import androidx.activity.compose.setContent;
import androidx.compose.material3.MaterialTheme;
import androidx.compose.material3.Surface;
import androidx.compose.runtime.Composable;
import androidx.compose.ui.tooling.preview.Preview;
import com.example.myapp.ui.theme.MyAppTheme;

public class MainActivity extends ComponentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContent {
            MyAppTheme {
                Surface(
                    color = MaterialTheme.colorScheme.background
                ) {
                    Greeting("Welcome to XDR Security App")
                }
            }
        }

        // Simulate data collection
        String logData = collectLogs();
        // Analyze logs for suspicious activities
        String analysisResult = analyzeLogs(logData);
        // Automate response based on analysis
        automateResponse(analysisResult);
    }

    private String collectLogs() {
        // Simulate log data collection
        return "Sample log data: suspicious_login_attempt";
    }

    private String analyzeLogs(String logData) {
        // Simulate log analysis
        if (logData.contains("suspicious_login_attempt")) {
            return "THREAT_DETECTED";
        }
        return "SAFE";
    }

    private void automateResponse(String analysisResult) {
        if (analysisResult.equals("THREAT_DETECTED")) {
            System.out.println("[ALERT] Threat detected. Taking action...");
            // Example: Generate alert, isolate the app, etc.
        }
    }

    @Composable
    void Greeting(String name) {
        androidx.compose.material3.Text(text = "Hello, " + name + "!")
    }

    @Preview(showBackground = true)
    @Composable
    void DefaultPreview() {
        MyAppTheme {
            Greeting("Android")
        }
    }
}
"""
main_activity_path = os.path.join(base_dir, "app/src/main/java/com/example/myapp/MainActivity.java")
create_file_if_not_exists(main_activity_path, main_activity_content)

# Create strings.xml for app strings
print("\nCreating strings.xml...")
strings_content = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">XDR Security App</string>
</resources>
"""
strings_path = os.path.join(base_dir, "app/src/main/res/values/strings.xml")
create_file_if_not_exists(strings_path, strings_content)

print("\nAndroid Studio project setup is complete. You can now import it and start building.")
