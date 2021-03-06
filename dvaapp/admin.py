from django.contrib import admin
from .models import Video,Frame,Detection,TEvent,IndexEntries,QueryResults,Query,Annotation,VLabel,VDNServer,VDNDataset,Export, S3Export, S3Import, ClusterCodes, Clusters


@admin.register(VLabel)
class AnnotationTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(QueryResults)
class QueryResultsAdmin(admin.ModelAdmin):
    pass


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    pass

@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexEntries)
class IndexEntriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin):
    pass


@admin.register(VDNServer)
class VDNServerAdmin(admin.ModelAdmin):
    pass


@admin.register(VDNDataset)
class VDNDatasetAdmin(admin.ModelAdmin):
    pass


@admin.register(TEvent)
class TEventAdmin(admin.ModelAdmin):
    pass


@admin.register(Export)
class ExportAdmin(admin.ModelAdmin):
    pass


@admin.register(S3Export)
class S3ExportAdmin(admin.ModelAdmin):
    pass


@admin.register(S3Import)
class S3ImportAdmin(admin.ModelAdmin):
    pass


@admin.register(Clusters)
class ClustersAdmin(admin.ModelAdmin):
    pass


@admin.register(ClusterCodes)
class ClusterCodesAdmin(admin.ModelAdmin):
    pass



