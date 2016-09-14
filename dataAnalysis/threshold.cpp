#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>
#include <stdio.h>
#include <vector>

using namespace cv;
using namespace std;
/// Global variables

int threshold_value = 0;
int threshold_type = 0;
int const max_value = 255;
int const max_type = 4;
int const max_BINARY_value = 255;

Mat src, src_hsv, dst, water_range,water,final_image;
char* window_name = "Threshold Demo";

/**
 * @function main
 */
int main( int argc, char** argv )
{
//Load an image
  src = imread( argv[1], 1 );
//imshow("Original1",src);
//Convert the image to Gray
  blur(src,src,Size(3,3), Point(-1,-1));
  blur(src,src,Size(3,3), Point(-1,-1));
  cvtColor( src, src_hsv, CV_BGR2HSV);
  inRange (src_hsv, Scalar(90,110,10), Scalar(130,255,150), water_range);
  imshow("HSV", src_hsv);
  imshow("Water",water_range);
  //cout<<"sizes: "<<src.size()<< "   "<< water_range.size()<<  endl;
  water.create(src.rows, src.cols, CV_8UC3);
  cout<<"sizes: "<<src.size()<< "   "<< water_range.size()<< "  "<< water.size()<< endl;
  for (int i=0; i<src.rows;i++)
  {
	for(int j=0;j<src.cols;j++)
	{
		if(water_range.at<uchar>(i,j) == 255)
		{
			 water.at<Vec3b>(i,j)[0] = 1;
			 water.at<Vec3b>(i,j)[1] = 1;
			 water.at<Vec3b>(i,j)[2] = 1;
		}
		
		else
		{
			 water.at<Vec3b>(i,j)[0] = 0;
			 water.at<Vec3b>(i,j)[1] = 0;
			 water.at<Vec3b>(i,j)[2] = 0;
		}
	}
  }

  imshow("Check", water);
  cout<<"check2"<< endl;


  //extraction(src,water_range);

  final_image = src.mul(water);
  //bitwise_and(src,water,final_image);
  cout<<"Check3"<< endl; 
 imshow("Final",final_image);
//  imshow("Original",src);

  /// Wait until user finishes program
  while(true)
  {
    int c;
    c = waitKey( 20 );
    if( (char)c == 27 )
      { break; }
   }

}

/*

 @function Threshold_Demo

 void Threshold_Demo( int, void* )
 {
      0: Binary
      1: Binary Inverted
      2: Threshold Truncated
      3: Threshold to Zero
      4: Threshold to Zero Inverted
   

   threshold( src_gray, dst, threshold_value, max_BINARY_value,threshold_type );

   imshow( window_name, dst );
 }*/
