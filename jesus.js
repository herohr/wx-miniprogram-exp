<import src="/components/trailerStars.vue.wxml" /><template name="85042c64">
	<view class="_view 85042c64 page">
		<swiper indicator-dots="{{true}}" autoplay="{{true}}" class="_swiper 85042c64 carousel">
			<swiper-item class="_swiper-item 85042c64">
				<image src="http://localhost:8000/static/carousel/batmanvssuperman.png" class="_image 85042c64 carousel"></image>
			</swiper-item>
			<swiper-item class="_swiper-item 85042c64">
				<image src="http://localhost:8000/static/carousel/spiderman.png" class="_image 85042c64 carousel"></image>
			</swiper-item>
		</swiper>
		<view class="_view 85042c64 page-block super-hot">
			<view class="_view 85042c64 hot-title-wapper">
				<image src="http://localhost:8000/static/icos/hot.png" class="_image 85042c64 hot-ico"></image>
				<view class="_view 85042c64 hot-title">热门超英</view>
			</view>
		</view>
		<scroll-view scroll-x="true" class="_scroll-view 85042c64 page-block hot">
			<view class="_view 85042c64 single-poster" wx:for="{{hotSuperheroList}}" wx:for-index="index" wx:for-item="superhero">
				<view class="_view 85042c64 poster-wapper">
					<navigator open-type="navigate" url="{{'../movie/movie?trailerId=' + superhero.id}}" class="_navigator 85042c64">
						<image src="{{superhero.cover}}" class="_image 85042c64 poster"></image>
					</navigator>
					<view class="_view 85042c64 movie-name">{{superhero.name}}</view><template showNum="1" data="{{...$root['0'], ...$root[$kk+'85042c64-2-'+index],$root}}"
					 is="383e188b"></template>
					<view class="_view 85042c64 movie-score-wapper">
						<image src="http://localhost:8000/static/icos/star-yellow.png" class="_image 85042c64 star-ico"></image>
						<image src="http://localhost:8000/static/icos/star-yellow.png" class="_image 85042c64 star-ico"></image>
						<image src="http://localhost:8000/static/icos/star-yellow.png" class="_image 85042c64 star-ico"></image>
						<image src="http://localhost:8000/static/icos/star-yellow.png" class="_image 85042c64 star-ico"></image>
						<image src="http://localhost:8000/static/icos/star-gray.png" class="_image 85042c64 star-ico"></image>
						<view class="_view 85042c64 movie-score">9.1</view>
					</view>
				</view>
			</view>
		</scroll-view>
		<view class="_view 85042c64 page-block super-hot">
			<view class="_view 85042c64 hot-title-wapper">
				<image src="http://localhost:8000/static/icos/interest.png" class="_image 85042c64 hot-ico"></image>
				<view class="_view 85042c64 hot-title">热门预告</view>
			</view>
		</view>
		<view class="_view 85042c64 hot-movies page-block"><video id="{{trailer.id}}" data-playingindex="{{trailer.id}}"
			 bindplay="handleProxy" src="{{trailer.trailer}}" poster="{{trailer.poster}}" class="_video 85042c64 hot-movie-single"
			 controls data-eventid="{{'85042c64-0-'+index}}" data-comkey="{{$k}}" wx:for="{{hotTrailerList}}" wx:for-index="index"
			 wx:for-item="trailer"></video></view>
		<view class="_view 85042c64 page-block super-hot">
			<view class="_view 85042c64 hot-title-wapper">
				<image src="http://localhost:8000/static/icos/guess-u-like.png" class="_image 85042c64 hot-ico"></image>
				<view class="_view 85042c64 hot-title">猜你喜欢</view>
			</view>
		</view>
		<view class="_view 85042c64 page-block guess-u-like">
			<view class="_view 85042c64 single-like-movie">
				<navigator open-type="navigate" url="../movie/movie-fake" class="_navigator 85042c64">
					<image src="http://localhost:8000/static/spider/cover.jpg" class="_image 85042c64 like-movie"></image>
				</navigator>
				<view class="_view 85042c64 movie-desc">
					<view class="_view 85042c64 movie-title">蜘蛛侠：英雄归来</view><template showNum="0" data="{{...$root['0'], ...$root[$kk+'85042c64-3'],$root}}"
					 is="383e188b"></template>
					<view class="_view 85042c64 movie-info">2018 / 美国 / 科幻 / 超级英雄</view>
					<view class="_view 85042c64 movie-info">上映时间：2017-09-08（中国大陆）</view>
				</view>
				<view class="_view 85042c64 movie-oper" bindtap="handleProxy" data-eventid="{{'85042c64-1'}}" data-comkey="{{$k}}" data-gindex="1">
					<image src="http://localhost:8000/static/icos/praise.png" class="_image 85042c64 praise-ico"></image>
					<view class="_view 85042c64 praise-me">点赞</view>
					<view animation="{{animationData}}" class="_view 85042c64 praise-me animation-opacity">+1</view>
				</view>
			</view>
		</view>
	</view>
</template>

