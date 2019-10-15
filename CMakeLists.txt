cmake_minimum_required(VERSION 3.4.1)

project(demo)
#引入两个变量 demo_BINARY_DIR  demo_SOURCE_DIR
#cmake自动定义两个等价变量PROJECT_BINARY_DIR PROJECT_SOURCE_DIR

set ( CMAKE_BUILD_TYPE "Debug" )

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    # ${CMAKE_CURRENT_BINARY_DIR}
    # ${CMAKE_CURRENT_SOURCE_DIR}/include
    )

#add_library 的用法
#-1-
#aux_source_directory(. SRC_LIST)                 #搜索当前目录下所有.cpp 文件列表存储在SRC_LIST中
#add_library(test_lib SHARED ${SRC_LIST})         #生成shared

#-2-
#add_library(test_lib SHARED test.cpp demo.cpp)   #明确指出包含哪些头源文件

#-3-
#file(GLOB SRC_LIST "*.cpp" "protocol/*.cpp")     #自定义搜索规则,1个LIST
#add_library(test_lib ${SRC_LIST})                #文件列表添加
#or
#file(GLOB SRC_LIST "*.cpp")                             #多个LIST
#file(GLOB SRC_PROTOCOL_LIST "protocol/*.cpp")
#add_library(test_lib ${SRC_LIST} ${SRC_PROTOCOL_LIST})  #文件列表添加
#or
#aux_source_directory(. SRC_LIST)                        #搜索多个目录下所有文件，多个LIST
#aux_source_directory(protocol SRC_PROTOCOL_LIST)
#add_library(test_lib ${SRC_LIST} ${SRC_PROTOCOL_LIST})  #文件列表添加


aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src SRC_LIST)#搜索当前目录下所有.cpp 文件列表存储在SRC_LIST中
add_library(test_shared SHARED ${SRC_LIST})
add_executable(test_go src/main.cpp)                         #生成可执行文件
target_link_libraries(test_go test_shared)               #链接

