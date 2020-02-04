//
//  AppLovinAd.h
//  sdk
//
//  Copyright (c) 2013, AppLovin Corporation. All rights reserved.


#import <Foundation/Foundation.h>
#import "ALAnnotations.h"

#import "ALAdSize.h"
#import "ALAdType.h"

AL_ASSUME_NONNULL_BEGIN

/**
 *  This class represents an ad that has been served from the AppLovin server and
 *  should be displayed to the user.
 */
@interface ALAd : NSObject <NSCopying>

/**
 * @name Ad Properties
 */

/**
 *  The size of this ad.
 */
@property (strong, nonatomic, readonly) ALAdSize *size;

/**
 *  The type of this ad.
 */
@property (strong, nonatomic, readonly) ALAdType *type;

/**
 *  The zone identifier for the ad, if any.
 */
@property (copy, nonatomic, readonly, alnullable) NSString *zoneIdentifier;

/**
 *  Whether or not the current ad is a video advertisement.
 */
@property (assign, readonly, getter=isVideoAd) BOOL videoAd;

/**
 * Get an arbitrary ad value for a given key. The list of keys may be found
 * in AppLovin documentation online.
 */
- (alnullable NSString *)adValueForKey:(NSString *)key;

/**
 * @name Ad Identification
 */

/**
 *  A unique ID which identifies this advertisement.
 *
 *  Should you need to report a broken ad to AppLovin support, please include this number's longValue.
 */
@property (strong, nonatomic, readonly) NSNumber *adIdNumber;

@end

@interface ALAd (ALDeprecated)
@property (strong, readonly, getter=size, alnullable) ALAdSize *adSize __deprecated_msg("Use size property instead.");
@property (strong, readonly, getter=type, alnullable) ALAdType *adType __deprecated_msg("Use type property instead.");
@end

AL_ASSUME_NONNULL_END
