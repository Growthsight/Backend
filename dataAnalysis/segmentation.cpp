#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>
#include <stdio.h>
#include <vector>

using namespace cv;
using namespace std;

int const max_value = 255;
int const max_type = 4;
int const max_BINARY_value = 255;

Mat src, src_hsv, dst, water_range,water,final_image;

int main( int argc, char** argv )
{
//Load an image
  src = imread( argv[1], 1 );
  blur(src,src,Size(3,3), Point(-1,-1));
  blur(src,src,Size(3,3), Point(-1,-1));
  cvtColor( src, src_hsv, CV_BGR2HSV);
  inRange (src_hsv, Scalar(90,110,10), Scalar(130,255,150), water_range);
  water.create(src.rows, src.cols, CV_8UC3);
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

  final_image = src.mul(water);
  if(imwrite(argv[1], final_image))
  	cout << "Success" << endl;
  else
        cout << "Error occurred" << endl;

}
