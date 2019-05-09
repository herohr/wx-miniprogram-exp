s = r"""<template name="383e188b">
	<view class="_view 383e188b movie-score-wapper">
		<image src="../../static/icos/star-yellow.png" class="_image 383e188b star-ico" wx:for="{{yelloScore}}" wx:for-index="index"
		 wx:for-item="yellow"></image>
		<image src="../../static/icos/star-gray.png" class="_image 383e188b star-ico" wx:for="{{grayScore}}" wx:for-index="index"
		 wx:for-item="gray"></image>
		<view class="_view 383e188b movie-score" wx:if="{{showNum == 1}}">{{innerScore}}</view>
	</view>
</template>
"""