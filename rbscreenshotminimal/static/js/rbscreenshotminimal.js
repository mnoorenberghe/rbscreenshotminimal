var RBScreenshotMinimal = {};

// Redirect from the dashboard to the open review list
if (window.location.pathname == "/dashboard/") {
    window.location = "/r/?show-closed=0";
}

RBScreenshotMinimal.Extension = RB.Extension.extend({
    initialize: function() {

        $(document).ready(function() {
            if (RB.DraftReviewBannerView) {
                RB.DraftReviewBannerView.prototype.show = function() {
                    // not showing banner and instead auto-publishing
                    this._onPublishClicked();
                };

                RB.DraftReviewBannerView.prototype.hideAndReload = function() {
                    // not going back to reviewURL
                };
            }
        });
    }
});
