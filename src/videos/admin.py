from django.contrib import admin

# Register your models here.
from .models import VideoAllProxy, VideoPublishedProxy

class VideoAdmin(admin.ModelAdmin):
  list_display = ['title', 'id', 'state', 'video_id', 'is_published', 'get_playlist_ids']
  search_fields = ['title']
  list_filter = ['state', 'active']
  readonly_fields = ['id', 'is_published', 'publish_timestamp', 'get_playlist_ids']
  class Meta:
    model = VideoAllProxy

  # def published(self, obj, *args, **kwargs):
  #   return obj.active

class VideoProxyAdmin(admin.ModelAdmin):
  list_display = ['title', 'video_id']
  search_fields = ['title']
  # list_filter = ['video_id']
  class Meta:
    model = VideoPublishedProxy

  def get_queryset(self, request):
    return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoAllProxy, VideoAdmin)
admin.site.register(VideoPublishedProxy, VideoProxyAdmin)